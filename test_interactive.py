# -*- coding: utf-8 -*-


from affectModel import *

DIR_A='AffectResources'
CommonWords = os.path.join(DIR_A, 'inp.txt')
CommonWordsCorrected = os.path.join(DIR_A,'corrects.txt')
MekMak = os.path.join(DIR_A,'mek-mak_stem_list.csv')
AfDic=os.path.join(DIR_A,'AffectDictionary.csv')
AfDicMarked=os.path.join(DIR_A,'AffectDictionaryMarked.csv')



list1=get_to_list(CommonWords)
list2=get_to_list(CommonWordsCorrected)
dicc=zip_to_dict(list1,list2)   
mekmak= get_to_list(MekMak)
normwords=get_input(AfDic)
markedwords=get_input(AfDicMarked)  
onlywords=[item[0] for item in normwords]
normwords=remove_mekmak(normwords,mekmak)   
affdic={item[0]:[float(item[2]),float(item[3]),float(item[4]),item[5]] for item in normwords}
markeddic={item[0]:[float(item[2]),float(item[3]),float(item[4]),item[5]] for item in markedwords}        
affdic=vowel_harmony(affdic, markeddic)
    
    
while 1:   

        inputtext = raw_input('Please enter text to see affective prediction: \n')        
        testing=inputtext.split()                    
        affdic=negate_sizsuz(testing,affdic)                 
        affect={}       
        repp = arousal_reps(testing)  
        upp = upper_case(testing) #check the letter case
        testing=[word.lower()  for word in testing]
       
        sentence=testing[:]
    
        testing=correction15000(dicc,testing)
        testing=remove_reps(testing,onlywords)
        sen_cleaned=testing[:]               
        emotion=check_emoticon(sentence)           
        affect=check_affect(affect,testing,affdic)
        affect=check_intensifiers(affect,sen_cleaned)
        affect,nene =check_negation(affect,sen_cleaned,affdic)
        polarity=check_polarity(affect)          
        valence,arousal,dominance=overall_average(affect,sen_cleaned,nene,emotion)
        valence,arousal,dominance= check_interjections(affect, polarity,valence,arousal,dominance)      
        valence,arousal,dominance= other_features(valence, arousal, dominance,repp,upp, polarity)        
        valence,arousal,dominance= put_limit(valence, arousal, dominance)
        

        
        print 'input text:', inputtext
        print 'normalized input:', " ".join(testing)
        print 'Word level analysis: '
        for a in affect:
            print a, affect[a]
        print 'Overall:',' Valence: ', valence, ' Arousal:', arousal, ' Dominance:', dominance
        print ' '
