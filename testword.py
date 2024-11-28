import cv2
import pytesseract
import numpy as np
#这是一个用于识别文字的副本，
# 由于其适用范围狭窄，
# 耗时较长，不支持识别杂乱页面，现已弃用

def preprocess_image(img):
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二值化
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary
def find_text_position(image_path, target_text):
    # 读取图像
    img = cv2.imread(image_path)
    if img is None:
        print("图像读取失败")
        return None

    img = preprocess_image(img)
    # 使用pytesseract进行OCR处理
    custom_config = r'--oem 3 --psm 11 -c tessedit_char_whitelist=0123456789'
    text_data = pytesseract.image_to_data(img, lang='chi_sim', config=custom_config, output_type=pytesseract.Output.DICT)

    # 找到目标文本的位置
    target_positions = []
    for i in range(len(text_data['text'])):
        if target_text in text_data['text'][i]:
            left = text_data['left'][i]
            top = text_data['top'][i]
            width = text_data['width'][i]
            height = text_data['height'][i]
            target_positions.append((left, top, left + width, top + height))

    if not target_positions:
        print("未找到目标文本")
        return None

    # 返回最佳匹配的位置（这里简化为返回第一个找到的位置）
    return target_positions[0]

# 使用示例
image_path = './DQH3.0/pictures/screenshot.png'
target_text = '暑期'

position = find_text_position(image_path, target_text)
if position:
    print(f"找到文本位置: {position}")
    # 这里可以添加代码来模拟鼠标点击
    # 例如使用pyautogui库
    # import pyautogui
    # pyautogui.click(position[0] + (position[2] - position[0]) // 2, position[1] + (position[3] - position[1]) // 2)