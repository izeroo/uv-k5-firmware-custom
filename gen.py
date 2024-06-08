import os
import time

def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

list1 = [
    'ENABLE_CHINESE_FULL=0',
    'ENABLE_CHINESE_FULL=4'
]

list2 = [
    'ENABLE_ENGLISH=1'
]

list3 = [
    'ENABLE_MESSENGER=1',
    'ENABLE_MESSENGER_DELIVERY_NOTIFICATION=1',
    'ENABLE_MESSENGER_NOTIFICATION=1'
]

list4 = [
    'ENABLE_DOPPLER=1',
]

list5 = [
    'ENABLE_MDC1200=1',
    'ENABLE_MDC1200_EDIT=1',
    'ENABLE_MDC1200_CONTACT=1'
]

list6 = [
    'ENABLE_4732=1',
    'ENABLE_FMRADIO=1'
]


list7 = [
    'ENABLE_PINYIN=1',
]

list8 = [
    'ENABLE_SPECTRUM=1'
]

listn = [
    list1,
    list2,
    list3,
    list4,
    list5,
    list6,
    list7
]

strx = []
stry = []

for chinese in list1:
    for messenger in [[], list3]:
        for doppler in [[], list4]:
            for mdc1200 in [[], list5]:
                for fm in [[], list6[0], list6[1]]:
                    for pinyin in [[],list7]:
                        for spectrum in [[],list8]:
                            strm = '';
                            strn = '';
                            strm += chinese + ' '
                            strn += chinese[-1]
                            if messenger != []:
                                strm += " ".join(list3) + ' '
                                strn += '1'
                            else:
                                strn += '0'
                            if doppler != []:
                                strm += " ".join(list4) + ' '
                                strn += '1'
                            else:
                                strn += '0'
                            if mdc1200 != []:
                                strm += " ".join(list5) + ' '
                                strn += '1'
                            else:
                                strn += '0'
                            if fm != []:
                                strm += fm + ' '
                                strn += fm[7]
                            else:
                                strn += '0'
                            if pinyin != []:
                                strm += " ".join(list7) + ' '
                                strn += '1'
                            else:
                                strn += '0'
                            if spectrum != []:
                                strm += " ".join(list8) + ' '
                                strn += '1'
                            else:
                                strn += '0'
                            strx.append(strm)
                            stry.append(strn)

for index in range(len(set(strx))):
    print(strx[index])
    print(stry[index])
    os.system("cp Makefile.template Makefile")
    alter("Makefile", "CUSCANSHU", strx[index])
    alter("Makefile", "CUSTOMNAME", 'LOSEHU' + stry[index])
    time.sleep(1)
    os.system("make all")