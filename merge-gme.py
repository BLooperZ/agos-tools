# -*- coding: windows-1255 -*-
import struct
import os

charMap = {'@': '�', 'A': '�', 'B': '�',
           'C': '�', 'D': '�', 'E': '�',
           'F': '�', 'G': '�', 'H': '�',
           'I': '�', 'J': '�', 'K': '�',
           'L': '�', 'M': '�', 'N': '�',
           'O': '�', 'P': '�', 'Q': '�',
           'R': '�', 'S': '�', 'T': '�',
           'U': '�', 'V': '�', 'W': '�',
           'X': '�', 'Y': '�', 'Z': '�'}

charMap = {v: k for k, v in charMap.iteritems()}

texts = os.listdir('texts')
files = os.listdir('temps')
textbins = files[366 : 366 + len(texts)]

for idx, text in enumerate(texts):
    with open('texts/' + text, 'rb') as textFile, open('temps/' + textbins[idx], 'wb') as binFile:
        lines = textFile.readlines()
        for line in lines:
            line = line.strip()
            line = ''.join(charMap[b] if b in charMap else b for b in line)
            binFile.write(line)
            binFile.write('\0')


files = os.listdir('temps')
with open('TEMP_DAT', 'wb') as datFile, open('TEMP_IDX', 'wb') as idxFile:
    num = len(files)
    size = num * 4
    idxFile.write(struct.pack('<I', size))
    for f in files[:-1]:
        with open('temps/' + f, 'rb') as tempFile:
            datFile.write(tempFile.read())
            size += tempFile.tell()
        idxFile.write(struct.pack('<I', size))
    with open('temps/' + files[-1], 'rb') as tempFile:
        datFile.write(tempFile.read())

with open('TEMP_DAT', 'rb') as datFile, open('TEMP_IDX', 'rb') as idxFile, open('SIMON-NEW.GME', 'wb') as gmeFile:
    gmeFile.write(idxFile.read())
    gmeFile.write(datFile.read())
