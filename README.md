# PicoW Hello

Raspberry Pi Pico W 初始化專案，使用 MicroPython 實作 WiFi 連線與 LED 控制。

## 功能

- **WiFi 連線**：連線至指定 SSID，支援連線逾時（預設 10 秒）
- **LED 控制**：啟動時板載 LED 持續閃爍，連線完成或逾時後停止並常亮
- **多執行緒**：WiFi 連線與 LED 閃爍同時進行，並透過 Lock 確保執行緒安全退出

## 檔案結構

```
hello/
└── app.py   # 主程式
```

## 使用方式

1. 修改 `app.py` 中的 WiFi 設定：

```python
ssid = "your_ssid"
passwd = "your_password"
```

2. 將 `app.py` 上傳至 Pico W（使用 Thonny 或 MicroPico）
3. 重啟裝置，程式自動執行

## 類別說明

### `WLAN`

| 方法 | 說明 |
|------|------|
| `connect(timeout=10)` | 連線至 WiFi，回傳 `True`（成功）或 `False`（逾時） |
| `disconnect()` | 斷線並關閉介面 |
| `is_connected()` | 回傳目前連線狀態 |
| `get_ip()` | 回傳裝置 IP 位址 |

### `LED`

| 方法 | 說明 |
|------|------|
| `on()` | 點亮 LED |
| `off()` | 關閉 LED |
| `toggle()` | 切換 LED 狀態 |

## 環境

- 裝置：Raspberry Pi Pico W
- 語言：MicroPython
