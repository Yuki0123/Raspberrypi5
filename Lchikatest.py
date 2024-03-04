import gpiod

# GPIO コントローラーチップ 0 を取得
chip = gpiod.Chip("0")

# GPIO ライン 26 を取得
line = chip.get_line(26)

# GPIO ライン 26 を出力として設定
line.request(gpiod.chip.DIRECTION_OUT)

# GPIO ライン 26 を HIGH に設定
line.set_value(1)

# GPIO ライン 26 を LOW に設定
line.set_value(0)