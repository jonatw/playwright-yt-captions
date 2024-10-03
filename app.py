from playwright.sync_api import sync_playwright

def download_youtube_captions(video_url):
    with sync_playwright() as p:
        # Connect to the browserless instance using CDP
        # browser = p.chromium.connect_over_cdp("ws://YOUR_PLAYWRIGHT_INSTANCE/chrome?token=YOUR_PLAYWRIGHT_TOKEN&launch={\"headless\":true}")
        # Or use the default browserless instance
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 旗標變數，用來標記是否已經下載完字幕
        subtitles_downloaded = False

        # 設置攔截器，僅攔截包含 "timedtext" 的字幕請求
        def handle_route(route):
            nonlocal subtitles_downloaded
            if 'timedtext' in route.request.url and 'lang' in route.request.url:
                try:
                    print(f"找到字幕 URL: {route.request.url}")
                    # 使用非阻塞方式獲取字幕內容
                    response = page.request.fetch(route.request)
                    subtitle_content = response.text()
                    # 保存字幕內容
                    with open("captions.json", "w", encoding="utf-8") as file:
                        file.write(subtitle_content)
                    print("字幕已成功下載並保存到 captions.json")
                    subtitles_downloaded = True  # 標記字幕已成功下載
                except Exception as e:
                    print(f"抓取字幕時發生錯誤: {str(e)}")
                finally:
                    route.continue_()

        # 只攔截包含 `timedtext` 的請求
        page.route("**/timedtext*", handle_route)

        # 進入 YouTube 影片頁面
        page.goto(video_url, timeout=60000)

        # 等待播放器的播放按鈕顯示
        page.wait_for_selector('.ytp-play-button')

        # 點擊播放按鈕開始播放影片
        page.click('.ytp-play-button')
        print("影片已播放")

        # 等待字幕按鈕顯示
        page.wait_for_selector('.ytp-subtitles-button')

        # 檢查字幕按鈕的 aria-pressed 狀態
        subtitle_button = page.locator('.ytp-subtitles-button')
        is_pressed = subtitle_button.get_attribute('aria-pressed')

        # 如果字幕未啟用，點擊按鈕啟用字幕
        if is_pressed == 'false':
            print("字幕未啟用，正在啟用...")
            subtitle_button.click()
        else:
            print("字幕已啟用")

        # 等待字幕載入，並在確定字幕已下載後關閉瀏覽器
        while not subtitles_downloaded:
            page.wait_for_timeout(1000)  # 等待一秒再檢查

        # 字幕下載完成後，關閉瀏覽器
        browser.close()
        print("瀏覽器已關閉，節省資源")

# 使用該函數來抓取字幕
download_youtube_captions('https://www.youtube.com/watch?v=Fw4JQdGHiIo')
