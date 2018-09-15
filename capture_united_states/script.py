
INPUT = [
    "edbbaacdcaacacbababaabadeeeaaddecaaeceeecbdcdaeacaccccaddeaaddecdcdcdccadcacceeecdcbceecebde",
    "dadbccabcdeccbcdbedaaabbdccdddcbdbebdeca",
    "aeaeddabaacbdcecacccbbacededbecbaccdccccebacdbbaedecbaeadaebedeccbaedcdcdabdcedbddabaeeaadcbdd",
    "abbdaedeeeedeaeeabcabbadbebedcedaadabbbddbbebdabecdcbdcc",
    "cddddabbaeaccaabedebbaaeabccecddcdbaaecbeeadeaeadabeddadaccbcdeebcacceaddabccdccaaddddd",
    "bbeeabcadeecbcadae",
    "dcbaceaadbdeceaaccaaeecadeedabeaecadbbebeecbdcddaadbbdbeecaaebcadddbb",
    "adcdeaccccaaeabaaeaaabeaecdbadbabdecadeeacebcdcceceebeecdeaeebbbccaeacedeaeddbd",
    "ed",
    "ebeecaddbbceecebdeadedecddddecddecebeabbbecabdbeddeceabc",
]

def init():
    
    for name in INPUT:
        TOTAL = 0
        sufixo = name
        
        while len(sufixo) >= 1:
            # print(sufixo, TOTAL)

            s = sufixo
            while len(s) >= 1:
                if name.startswith(s):
                    TOTAL += len(s)
                    break
                else:
                    s = s[:-1]
            
            sufixo = sufixo[1:]

        print(TOTAL)

init()
