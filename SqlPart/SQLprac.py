import pymysql

import sys


def remove_non_utf8(input_str):
    """
    Removes non-UTF-8 characters from a string.

    Args:
        input_str (str): The input string.

    Returns:
        str: The string with non-UTF-8 characters removed.
    """
    cleaned_bytes = bytes([byte for byte in input_str.encode('utf-8', errors='replace') if byte != 0x3f])
    cleaned_str = cleaned_bytes.decode('utf-8')
    return cleaned_str

def writeInto(name,SteamPrice,uuPrice):
    name =  remove_non_utf8(name)
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           passwd='nao2004', db='daxulaoshi_try1', charset='utf8')
    cursor = conn.cursor()
    cursor.execute(f"insert into BtPrice(name,SteamPrice,UUPrice) values('{name}', {SteamPrice},{uuPrice});")
    conn.commit()

    cursor.close()
