
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
            
    