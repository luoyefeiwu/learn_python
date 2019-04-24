# coding=utf-8

# 屏幕中央打印字符串

sentence = input('Sentence:')

screen_with = 80;
text_width = len(sentence)
box_width = text_width + 7
left_margin = (screen_with - box_width) // 2

print()
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
print(' '*left_margin+'|')
