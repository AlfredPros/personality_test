
default personality_scoreE = 20
default personality_scoreA = 14
default personality_scoreC = 14
default personality_scoreN = 38
default personality_scoreO = 8

screen ask_question(var_name, behavior, goto):
    modal True
    style_prefix "choice"

    if behavior == "plus":
        vbox:
            textbutton "disagree":
                action SetVariable(var_name, eval(var_name)+1), Hide(), Jump(goto)
            textbutton "slightly disagree":
                action SetVariable(var_name, eval(var_name)+2), Hide(), Jump(goto)
            textbutton "neutral":
                action SetVariable(var_name, eval(var_name)+3), Hide(), Jump(goto)
            textbutton "slightly agree":
                action SetVariable(var_name, eval(var_name)+4), Hide(), Jump(goto)
            textbutton "agree":
                action SetVariable(var_name, eval(var_name)+5), Hide(), Jump(goto)
    else:
        vbox:
            textbutton "disagree":
                action SetVariable(var_name, eval(var_name)-1), Hide(), Jump(goto)
            textbutton "slightly disagree":
                action SetVariable(var_name, eval(var_name)-2), Hide(), Jump(goto)
            textbutton "neutral":
                action SetVariable(var_name, eval(var_name)-3), Hide(), Jump(goto)
            textbutton "slightly agree":
                action SetVariable(var_name, eval(var_name)-4), Hide(), Jump(goto)
            textbutton "agree":
                action SetVariable(var_name, eval(var_name)-5), Hide(), Jump(goto)

label start:
    
    show screen ask_question("personality_scoreE", "plus", "q2")
    
    "1. Am the life of the party"
    
label q2:
    
    show screen ask_question("personality_scoreA", "minus", "q3")
    
    "2. Feel little concern for others."
    
label q3:

    show screen ask_question("personality_scoreC", "plus", "q4")
    
    "3. Am always prepared."
    
label q4:
    
    show screen ask_question("personality_scoreN", "minus", "q5")
    
    "4. Get stressed out easily."
    
label q5:
    
    show screen ask_question("personality_scoreO", "plus", "q6")
    
    "5. Have a rich vocabulary. "

label q6:
    
    show screen ask_question("personality_scoreE", "minus", "q7")
    
    "6. Don't talk a lot."
    
label q7:
    
    show screen ask_question("personality_scoreA", "plus", "q8")
    
    "7. Am interested in people."

label q8:
    
    show screen ask_question("personality_scoreC", "minus", "q9")
    
    "8. Leave my belongings around."
    
label q9:
    
    show screen ask_question("personality_scoreN", "plus", "q10")
    
    "9. Am relaxed most of the time."

label q10:
    
    show screen ask_question("personality_scoreO", "minus", "q11")
    
    "10. Have difficulty understanding abstract ideas. "
    
label q11:
    
    show screen ask_question("personality_scoreE", "plus", "q12")
    
    "11. Feel comfortable around people."
    
label q12:
    
    show screen ask_question("personality_scoreA", "minus", "q13")
    
    "12. Insult people"
    
label q13:
    
    show screen ask_question("personality_scoreC", "plus", "q14")
    
    "13. Pay attention to details."
   
label q14:
    
    show screen ask_question("personality_scoreN", "minus", "q15")
    
    "14. Worry about things."
    
label q15:
    
    show screen ask_question("personality_scoreO", "plus", "q16")
    
    "15. Have a vivid imagination."

label q16:
    
    show screen ask_question("personality_scoreE", "minus", "q17")
    
    "16. Keep in the background."

label q17:
    
    show screen ask_question("personality_scoreA", "plus", "q18")
    
    "17. Sympathize with others' feelings. "

label q18:
    
    show screen ask_question("personality_scoreC", "minus", "q19")
    
    "18. Make a mess of things."

label q19:
    
    show screen ask_question("personality_scoreN", "plus", "q20")
    
    "19. Seldom feel blue."

label q20:

    show screen ask_question("personality_scoreO", "minus", "q21")
    
    "20. Am not interested in abstract ideas." 

label q21:

    show screen ask_question("personality_scoreE", "plus", "q22")
    
    "21. Start conversations. "

label q22:

    show screen ask_question("personality_scoreA", "minus", "q23")
    
    "22. Am not interested in other people's problems." 

label q23:

    show screen ask_question("personality_scoreC", "plus", "q24")
    
    "23. Get chores done right away."

label q24:

    show screen ask_question("personality_scoreN", "minus", "q25")
    
    "24. Am easily disturbed."

label q25:

    show screen ask_question("personality_scoreO", "plus", "q26")
    
    "25. Have excellent ideas." 

label q26:

    show screen ask_question("personality_scoreE", "minus", "q27")
    
    "26. Have little to say."  

label q27:

    show screen ask_question("personality_scoreA", "plus", "q28")
    
    "27. Have a soft heart."  

label q28:

    show screen ask_question("personality_scoreC", "minus", "q29")
    
    "28. Often forget to put things back in their proper place." 

label q29:

    show screen ask_question("personality_scoreN", "minus", "q30")
    
    "29. Get upset easily."

label q30:

    show screen ask_question("personality_scoreO", "minus", "q31")
    
    "30. Do not have a good imagination."

label q31:

    show screen ask_question("personality_scoreE", "plus", "q32")
    
    "31. Talk to a lot of different people at parties."

label q32:

    show screen ask_question("personality_scoreA", "minus", "q33")
    
    "32. Am not really interested in others."

label q33:

    show screen ask_question("personality_scoreC", "plus", "q34")
    
    "33. Like order."

label q34:

    show screen ask_question("personality_scoreN", "minus", "q35")
    
    "34. Change my mood a lot."
    
label q35:
    
    show screen ask_question("personality_scoreO", "plus", "q36")
    
    "35. Am quick to understand things."

label q36:
    
    show screen ask_question("personality_scoreE", "minus", "q37")
    
    "36. Don't like to draw attention to myself."

label q37:
    
    show screen ask_question("personality_scoreA", "plus", "q38")
    
    "37. Take time out for others."

label q38:
    
    show screen ask_question("personality_scoreC", "minus", "q39")
    
    "38. Shirk my duties."

label q39:
    
    show screen ask_question("personality_scoreN", "minus", "q40")
    
    "39. Have frequent mood swings."

label q40:
    
    show screen ask_question("personality_scoreO", "plus", "q41")
    
    "40. Use difficult words."

label q41:
    
    show screen ask_question("personality_scoreE", "plus", "q42")
    
    "41. Don't mind being the center of attention."

label q42:
    
    show screen ask_question("personality_scoreA", "plus", "q43")
    
    "42. Feel others' emotions."

label q43:
    
    show screen ask_question("personality_scoreC", "plus", "q44")
    
    "43. Follow a schedule."

label q44:
    
    show screen ask_question("personality_scoreN", "minus", "q45")
    
    "44. Get irritated easily."

label q45:
    
    show screen ask_question("personality_scoreO", "plus", "q46")
    
    "45.  Spend time reflecting on things."

label q46:
    
    show screen ask_question("personality_scoreE", "minus", "q47")
    
    "46. Am quiet around strangers."

label q47:
    
    show screen ask_question("personality_scoreA", "plus", "q48")
    
    "47. Make people feel at ease."

label q48:
    
    show screen ask_question("personality_scoreC", "plus", "q49")
    
    "48. Am exacting in my work."

label q49:
    
    show screen ask_question("personality_scoreN", "minus", "q50")
    
    "49. Often feel blue."
    
label q50:
    
    show screen ask_question("personality_scoreO", "plus", "result")
    
    "50. Am full of ideas."

label result:

    "Total: E:[personality_scoreE] A:[personality_scoreA] C:[personality_scoreC] N:[personality_scoreN] O:[personality_scoreO]"
    
    return
    