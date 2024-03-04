import gpiod

# GPIO コントローラーチップ 0 を取得
chip = gpiod.Chip('0')

# GPIO ライン 25 を取得
line = chip.get_line(26)

# GPIO ライン 25 を出力として設定
#line.request(gpiod.LINE_REQUEST_DIRECTION_OUT)
line.request(chip.LINE_REQUEST_DIRECTION_OUT)

# 無限ループで点滅
while True:
  # GPIO ライン 25 を HIGH に設定
  line.set_value(1)

  # 1 秒間待つ
  time.sleep(1)

  # GPIO ライン 25 を LOW に設定
  line.set_value(0)

  # 1 秒間待つ
  time.sleep(1)