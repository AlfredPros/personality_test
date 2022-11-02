
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
    
    "Total: [personality_scoreE] [personality_scoreA] [personality_scoreC] [personality_scoreN] [personality_scoreO]"
    
    return
            
    