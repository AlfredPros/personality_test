
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
    
    show screen ask_question("personality_scoreO", "plus", "q51")
    
    "50. Am full of ideas."

label q51:

    "Total: [personality_scoreE] [personality_scoreA] [personality_scoreC] [personality_scoreN] [personality_scoreO]"
    
    return
    