def test_mode_ita(images=False, answers=False):
    if images is True and answers is False:
        imgs = {}
        for c in range(1, 91):
            imgs[c] = f'Imagens/ITA 2023/{c}.png'
        return imgs
    elif answers is True and images is False:
        answers = {1: 'd',
                   2: 'e',
                   3: 'e',
                   4: 'c',
                   5: 'c',
                   6: 'nenhuma',
                   7: 'b',
                   8: 'c',
                   9: 'e',
                   10: 'e',
                   11: 'b',
                   12: 'd',
                   13: 'e',
                   14: 'b',
                   15: 'b',
                   16: 'e',
                   17: 'a',
                   18: 'nenhuma',
                   19: 'b',
                   20: 'd',
                   21: 'b',
                   22: 'e',
                   23: 'a',
                   24: 'c',
                   25: 'a',
                   26: 'd',
                   27: 'd',
                   28: 'b',
                   29: 'b',
                   30: 'e',
                   31: 'd',
                   32: 'b',
                   33: 'b',
                   34: 'b',
                   35: 'd',
                   36: 'c',
                   37: 'c',
                   38: 'e',
                   39: 'b',
                   40: 'c',
                   41: 'b',
                   42: 'd',
                   43: 'd',
                   44: 'a',
                   45: 'b',
                   46: 'e',
                   47: 'a',
                   48: 'c',
                   49: 'e',
                   50: 'c',
                   51: 'b',
                   52: 'd',
                   53: 'd',
                   54: 'a',
                   55: 'a',
                   56: 'c',
                   57: 'e',
                   58: 'b',
                   59: 'a',
                   60: 'b'}
        return answers
    else:
        return 'Error: Select just one option'

#anuladas enem: 1

def test_mode_enem(images=False, english=False, spanish=False, answers=False):
    if images is True and answers is False:
        imgs = {}
        if (english is True) and (spanish is False):
            for c in range(1, 6):
                imgs[c] = f'Imagens/ENEM 2022 CADERNOS AZUIS/1 DIA/1-5 Inglês/{c}.png'
            for c in range(6, 91):
                imgs[c] = f'Imagens/ENEM 2022 CADERNOS AZUIS/1 DIA/6-90/{c}.png'
        elif (spanish is True) and (english is False):
            for c in range(1, 6):
                imgs[c] = f'Imagens/ENEM 2022 CADERNOS AZUIS/1 DIA/1-5 Espanhol/{c}.png'
            for c in range(6, 91):
                imgs[c] = f'Imagens/ENEM 2022 CADERNOS AZUIS/1 DIA/6-90/{c}.png'
        else:
            return 'Error: Select just one option'
        for c in range(91, 181):
            imgs[c] = f'Imagens/ENEM 2022 CADERNOS AZUIS/2 DIA/{c}.png'
        return imgs
    elif answers is True and images is False:
        if (english is True) and (spanish is False):
            answers = {1: 'd',
                       2: 'c',
                       3: 'b',
                       4: 'd',
                       5: 'e',
                       6: 'e',
                       7: 'a',
                       8: 'a',
                       9: 'a',
                       10: 'c',
                       11: 'a',
                       12: 'b',
                       13: 'b',
                       14: 'd',
                       15: 'b',
                       16: 'e',
                       17: 'b',
                       18: 'a',
                       19: 'c',
                       20: 'c',
                       21: 'b',
                       22: 'e',
                       23: 'e',
                       24: 'e',
                       25: 'c',
                       26: 'c',
                       27: 'b',
                       28: 'b',
                       29: 'd',
                       30: 'c',
                       31: 'a',
                       32: 'a',
                       33: 'a',
                       34: 'd',
                       35: 'c',
                       36: 'c',
                       37: 'a',
                       38: 'b',
                       39: 'e',
                       40: 'd',
                       41: 'b',
                       42: 'd',
                       43: 'e',
                       44: 'c',
                       45: 'e',
                       46: 'd',
                       47: 'e',
                       48: 'a',
                       49: 'b',
                       50: 'e',
                       51: 'e',
                       52: 'd',
                       53: 'a',
                       54: 'e',
                       55: 'b',
                       56: 'a',
                       57: 'a',
                       58: 'e',
                       59: 'c',
                       60: 'b',
                       61: 'e',
                       62: 'c',
                       63: 'b',
                       64: 'c',
                       65: 'b',
                       66: 'c',
                       67: 'd',
                       68: 'd',
                       69: 'a',
                       70: 'a',
                       71: 'a',
                       72: 'd',
                       73: 'b',
                       74: 'c',
                       75: 'e',
                       76: 'd',
                       77: 'a',
                       78: 'e',
                       79: 'a',
                       80: 'c',
                       81: 'd',
                       82: 'b',
                       83: 'b',
                       84: 'c',
                       85: 'd',
                       86: 'c',
                       87: 'b',
                       88: 'e',
                       89: 'c',
                       90: 'a',
                       91: 'a',
                       92: 'd',
                       93: 'b',
                       94: 'a',
                       95: 'd',
                       96: 'a',
                       97: 'b',
                       98: 'e',
                       99: 'a',
                       100: 'b',
                       101: 'c',
                       102: 'e',
                       103: 'e',
                       104: 'e',
                       105: 'a',
                       106: 'c',
                       107: 'c',
                       108: 'b',
                       109: 'd',
                       110: 'd',
                       111: 'a',
                       112: 'd',
                       113: 'd',
                       114: 'c',
                       115: 'b',
                       116: 'b',
                       117: 'c',
                       118: 'c',
                       119: 'a',
                       120: 'e',
                       121: 'b',
                       122: 'a',
                       123: 'e',
                       124: 'b',
                       125: 'e',
                       126: 'b',
                       127: 'e',
                       128: 'a',
                       129: 'c',
                       130: 'c',
                       131: 'c',
                       132: 'd',
                       133: 'd',
                       134: 'd',
                       135: 'e',
                       136: 'e',
                       137: 'c',
                       138: 'd',
                       139: 'a',
                       140: 'b',
                       141: 'e',
                       142: 'b',
                       143: 'd',
                       144: 'c',
                       145: 'e',
                       146: 'e',
                       147: 'c',
                       148: 'd',
                       149: 'b',
                       150: 'd',
                       151: 'c',
                       152: 'c',
                       153: 'c',
                       154: 'c',
                       155: 'b',
                       156: 'c',
                       157: 'nenhuma',
                       158: 'c',
                       159: 'b',
                       160: 'a',
                       161: 'a',
                       162: 'c',
                       163: 'd',
                       164: 'b',
                       165: 'a',
                       166: 'a',
                       167: 'a',
                       168: 'c',
                       169: 'e',
                       170: 'b',
                       171: 'a',
                       172: 'b',
                       173: 'd',
                       174: 'd',
                       175: 'e',
                       176: 'd',
                       177: 'a',
                       178: 'e',
                       179: 'b',
                       180: 'e'}
        elif (spanish is True) and (english is False):
            answers = {1: 'e',
                       2: 'd',
                       3: 'c',
                       4: 'a',
                       5: 'a',
                       6: 'e',
                       7: 'a',
                       8: 'a',
                       9: 'a',
                       10: 'c',
                       11: 'a',
                       12: 'b',
                       13: 'b',
                       14: 'd',
                       15: 'b',
                       16: 'e',
                       17: 'b',
                       18: 'a',
                       19: 'c',
                       20: 'c',
                       21: 'b',
                       22: 'e',
                       23: 'e',
                       24: 'e',
                       25: 'c',
                       26: 'c',
                       27: 'b',
                       28: 'b',
                       29: 'd',
                       30: 'c',
                       31: 'a',
                       32: 'a',
                       33: 'a',
                       34: 'd',
                       35: 'c',
                       36: 'c',
                       37: 'a',
                       38: 'b',
                       39: 'e',
                       40: 'd',
                       41: 'b',
                       42: 'd',
                       43: 'e',
                       44: 'c',
                       45: 'e',
                       46: 'd',
                       47: 'e',
                       48: 'a',
                       49: 'b',
                       50: 'e',
                       51: 'e',
                       52: 'd',
                       53: 'a',
                       54: 'e',
                       55: 'b',
                       56: 'a',
                       57: 'a',
                       58: 'e',
                       59: 'c',
                       60: 'b',
                       61: 'e',
                       62: 'c',
                       63: 'b',
                       64: 'c',
                       65: 'b',
                       66: 'c',
                       67: 'd',
                       68: 'd',
                       69: 'a',
                       70: 'a',
                       71: 'a',
                       72: 'd',
                       73: 'b',
                       74: 'c',
                       75: 'e',
                       76: 'd',
                       77: 'a',
                       78: 'e',
                       79: 'a',
                       80: 'c',
                       81: 'd',
                       82: 'b',
                       83: 'b',
                       84: 'c',
                       85: 'd',
                       86: 'c',
                       87: 'b',
                       88: 'e',
                       89: 'c',
                       90: 'a',
                       91: 'a',
                       92: 'd',
                       93: 'b',
                       94: 'a',
                       95: 'd',
                       96: 'a',
                       97: 'b',
                       98: 'e',
                       99: 'a',
                       100: 'b',
                       101: 'c',
                       102: 'e',
                       103: 'e',
                       104: 'e',
                       105: 'a',
                       106: 'c',
                       107: 'c',
                       108: 'b',
                       109: 'd',
                       110: 'd',
                       111: 'a',
                       112: 'd',
                       113: 'd',
                       114: 'c',
                       115: 'b',
                       116: 'b',
                       117: 'c',
                       118: 'c',
                       119: 'a',
                       120: 'e',
                       121: 'b',
                       122: 'a',
                       123: 'e',
                       124: 'b',
                       125: 'e',
                       126: 'b',
                       127: 'e',
                       128: 'a',
                       129: 'c',
                       130: 'c',
                       131: 'c',
                       132: 'd',
                       133: 'd',
                       134: 'd',
                       135: 'e',
                       136: 'e',
                       137: 'c',
                       138: 'd',
                       139: 'a',
                       140: 'b',
                       141: 'e',
                       142: 'b',
                       143: 'd',
                       144: 'c',
                       145: 'e',
                       146: 'e',
                       147: 'c',
                       148: 'd',
                       149: 'b',
                       150: 'd',
                       151: 'c',
                       152: 'c',
                       153: 'c',
                       154: 'c',
                       155: 'b',
                       156: 'c',
                       157: 'nenhuma',
                       158: 'c',
                       159: 'b',
                       160: 'a',
                       161: 'a',
                       162: 'c',
                       163: 'd',
                       164: 'b',
                       165: 'a',
                       166: 'a',
                       167: 'a',
                       168: 'c',
                       169: 'e',
                       170: 'b',
                       171: 'a',
                       172: 'b',
                       173: 'd',
                       174: 'd',
                       175: 'e',
                       176: 'd',
                       177: 'a',
                       178: 'e',
                       179: 'b',
                       180: 'e'}
        else:
            pass
        return answers
    else:
        return 'Error: Select just one option'

# anuladas fuvest: 1

def test_mode_fuvest(images=False, answers=False):
    if images is True and answers is False:
        imgs = {}
        for c in range(1, 91):
            imgs[c] = f'Imagens/FUVEST 2022 PROVA V/{c}.png'
        return imgs
    elif answers is True and images is False:
        answers = {1: 'c',
                   2: 'c',
                   3: 'e',
                   4: 'b',
                   5: 'd',
                   6: 'a',
                   7: 'b',
                   8: 'c',
                   9: 'e',
                   10: 'b',
                   11: 'a',
                   12: 'a',
                   13: 'c',
                   14: 'b',
                   15: 'd',
                   16: 'd',
                   17: 'e',
                   18: 'a',
                   19: 'd',
                   20: 'd',
                   21: 'e',
                   22: 'c',
                   23: 'e',
                   24: 'a',
                   25: 'd',
                   26: 'c',
                   27: 'a',
                   28: 'b',
                   29: 'b',
                   30: 'c',
                   31: 'a',
                   32: 'c',
                   33: 'c',
                   34: 'd',
                   35: 'b',
                   36: 'e',
                   37: 'a',
                   38: 'e',
                   39: 'b',
                   40: 'd',
                   41: 'd',
                   42: 'b',
                   43: 'd',
                   44: 'c',
                   45: 'e',
                   46: 'c',
                   47: 'd',
                   48: 'c',
                   49: 'e',
                   50: 'c',
                   51: 'b',
                   52: 'd',
                   53: 'd',
                   54: 'nenhuma',
                   55: 'c',
                   56: 'a',
                   57: 'd',
                   58: 'e',
                   59: 'd',
                   60: 'c',
                   61: 'b',
                   62: 'b',
                   63: 'a',
                   64: 'd',
                   65: 'e',
                   66: 'd',
                   67: 'a',
                   68: 'a',
                   69: 'b',
                   70: 'd',
                   71: 'c',
                   72: 'd',
                   73: 'a',
                   74: 'c',
                   75: 'b',
                   76: 'e',
                   77: 'e',
                   78: 'a',
                   79: 'b',
                   80: 'a',
                   81: 'd',
                   82: 'c',
                   83: 'a',
                   84: 'c',
                   85: 'c',
                   86: 'a',
                   87: 'a',
                   88: 'a',
                   89: 'e',
                   90: 'a'}
        return answers
    else:
        return 'Error: Select just one option'