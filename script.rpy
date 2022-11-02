
default personality_scoreE = 20
default personality_scoreA = 14
default personality_scoreC = 14
default personality_scoreN = 38
default personality_scoreO = 8

screen ask_question(var_name, behavior, goto):
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

    "Total: [personality_scoreE] [personality_scoreA] [personality_scoreC] [personality_scoreN] [personality_scoreO]"

    return
            
    