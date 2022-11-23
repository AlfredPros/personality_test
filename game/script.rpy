
# E-O: max:40 min:0
define E_BOUNDARY = 19.7
define A_BOUNDARY = 27.6
define C_BOUNDARY = 23.5
define N_BOUNDARY = 19.4
define O_BOUNDARY = 28.7

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
            textbutton "Disagree":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_1.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)+1), Hide(), Jump(goto)
            textbutton "Slightly disagree":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_2.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)+2), Hide(), Jump(goto)
            textbutton "Neutral":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_3.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)+3), Hide(), Jump(goto)
            textbutton "Slightly agree":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_4.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)+4), Hide(), Jump(goto)
            textbutton "Agree":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_5.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)+5), Hide(), Jump(goto)
    else:
        vbox:
            textbutton "Disagree":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_1.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)-1), Hide(), Jump(goto)
            textbutton "Slightly disagree":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_2.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)-2), Hide(), Jump(goto)
            textbutton "Neutral":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_3.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)-3), Hide(), Jump(goto)
            textbutton "Slightly agree":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_4.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)-4), Hide(), Jump(goto)
            textbutton "Agree":
                background "gui/button/choice_idle_background.png"
                hover_background "gui/button/choice_hover_background_5.png"
                text_hover_color "#202225"
                action SetVariable(var_name, eval(var_name)-5), Hide(), Jump(goto)

label start:
    
    stop music fadeout 2
    
    scene fill with Dissolve(1)
    
    "Welcome to Big Five Personality Test!"
    
    "You will be asked 50 questions and be given 5 choices from agree to disagree."
    
    "Please answer them honestly, so we can understand your personality better."
    
    "Without further ado, let's begin!"
    
    scene 495521 with Dissolve(1)
    
    show screen ask_question("personality_scoreE", "plus", "q2") with Dissolve(0.125)
    
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
    
    scene 743487 with Dissolve(1)
    
    show screen ask_question("personality_scoreE", "minus", "q7") with Dissolve(0.125)
    
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
    
    scene 777726 with Dissolve(1)
    
    show screen ask_question("personality_scoreE", "plus", "q12") with Dissolve(0.125)
    
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
    
    scene 861598 with Dissolve(1)
    
    show screen ask_question("personality_scoreE", "minus", "q17") with Dissolve(0.125)
    
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
    
    scene 861665 with Dissolve(1)

    show screen ask_question("personality_scoreE", "plus", "q22") with Dissolve(0.125)
    
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
    
    scene 861741 with Dissolve(1)

    show screen ask_question("personality_scoreE", "minus", "q27") with Dissolve(0.125)
    
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
    
    scene 861767 with Dissolve(1)

    show screen ask_question("personality_scoreE", "plus", "q32") with Dissolve(0.125)
    
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
    
    scene 861908 with Dissolve(1)
    
    show screen ask_question("personality_scoreE", "minus", "q37") with Dissolve(0.125)
    
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
    
    scene 862020 with Dissolve(1)
    
    show screen ask_question("personality_scoreE", "plus", "q42") with Dissolve(0.125)
    
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
    
    scene 862056 with Dissolve(1)
    
    show screen ask_question("personality_scoreE", "minus", "q47") with Dissolve(0.125)
     
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
    
    
screen stats():
    
    python:
        E_p = personality_scoreE/40.0*100.0
        A_p = personality_scoreA/40.0*100.0
        C_p = personality_scoreC/40.0*100.0
        N_p = personality_scoreN/40.0*100.0
        O_p = personality_scoreO/40.0*100.0
        
        if (personality_scoreE > E_BOUNDARY):
            E_c = "#C1FFC1"
        else:
            E_c = "#FFC1C1"
        if (personality_scoreA > A_BOUNDARY):
            A_c = "#C1FFC1"
        else:
            A_c = "#FFC1C1"
        if (personality_scoreC > C_BOUNDARY):
            C_c = "#C1FFC1"
        else:
            C_c = "#FFC1C1"
        if (personality_scoreN > N_BOUNDARY):
            N_c = "#C1FFC1"
        else:
            N_c = "#FFC1C1"
        if (personality_scoreO > O_BOUNDARY):
            O_c = "#C1FFC1"
        else:
            O_c = "#FFC1C1"
        
    
    text "Your Final Score":
        align(0.5, 0.125)
        size 52
        color "#37342F"
    
    # E
    text "Extraversion: [E_p]%":
        align(0.32, 0.25)
        color "#37342F"
    bar:
        left_bar Solid(E_c)
        align(0.325, 0.297)
        ysize 50
        xsize 280
        value AnimatedValue(value=personality_scoreE, range=40, delay=0.5, old_value=0)
        
    # A
    text "Agreeableness: [A_p]%":
        align(0.69, 0.25)
        color "#37342F"
    bar:
        left_bar Solid(A_c)
        align(0.675, 0.297)
        ysize 50
        xsize 280
        value AnimatedValue(value=personality_scoreA, range=40, delay=0.5, old_value=0)
        
    # C
    text "Conscientiousness: [C_p]%":
        align(0.32, 0.4)
        color "#37342F"
    bar:
        left_bar Solid(C_c)
        align(0.325, 0.447)
        ysize 50
        xsize 280
        value AnimatedValue(value=personality_scoreC, range=40, delay=0.5, old_value=0)
        
    # N
    text "Neuroticism: [N_p]%":
        align(0.68, 0.4)
        color "#37342F"
    bar:
        left_bar Solid(N_c)
        align(0.675, 0.447)
        ysize 50
        xsize 280
        value AnimatedValue(value=personality_scoreN, range=40, delay=0.5, old_value=0)
        
    # O
    text "Openness: [O_p]%":
        align(0.5, 0.55)
        color "#37342F"
    bar:
        left_bar Solid(O_c)
        align(0.5, 0.597)
        ysize 50
        xsize 280
        value AnimatedValue(value=personality_scoreO, range=40, delay=0.5, old_value=0)

label result:
    
    scene fill with Dissolve(1)
    
    "This is the end of the personality test. Good job for answering all of them!\n\nContinue to know the result."
    
    "Based on the score, we predict that you..."
    
    show screen stats with Dissolve(0.25)
    
    if personality_scoreE > E_BOUNDARY:  # high
        "You have a high level of extraversion. That means you,\n- Seek excitement or adventure\n- Make friends easily"
        "- Speak without thinking\n- And enjoy being active with others"

        "You might consider yourself an extrovert. 
        \nYou might enjoy attention and feel recharged after spending time with friends. 
        \nYou likely feel your best when in a large group of people. "
        "On the other hand, you may have trouble spending long periods of time alone."
        
    else: # low
        "You have a low level of extraversion, which means you\n- Have a hard time making small talk or introducing yourself\n- Feel worn out after socializing"
        "- Avoid large groups\n- And are more reserved"

        "A low extraversion score can mean you prefer to spend time alone or with a small group of close friends. 
        \nYou might also be a more private person when it comes to sharing details about your life. "
        "This might come across as somewhat cold to others"

        
    if personality_scoreA > A_BOUNDARY:  # high
        "You have a high level of agreeableness. That means you are,\n- Always ready to help out\n- Caring and honest"
        "- Interested in the people around you\n- And believe the best about others"

        "A high agreeableness may also means you're helpful and cooperative. 
        \nYour loved ones may often turn to you for help. 
        \nPeople might see you as trustworthy. "
        "You may be the person others seek when they're trying to resolve a disagreement. 
        \nIn some situations, you might a little too trusting or willing to compromise."
        "Try to balance your knack for pleasing others with self-advocacy."
        
    else: # low
        "You have a low level of agreeableness, which means you are\n- Stubborn\n- Find it difficult to forgive mistakes"
        "- Self-centered\n- And have less compassion for others"

        "A low agreeableness score may mean you tend hold grudges. 
        \nYou might also be less sympathetic with others. 
        \nBut you are also likely avoid the pitfalls of comparing yourself to others or caring about what others think of you."
        
        
    if personality_scoreC > C_BOUNDARY:  # high
        "You have a high level of conscientiousness. That means you,\n- Keep things in order\n- Come prepared to school or work"
        "- Are goal-driven\n- And are persistent"

        "You have a high level of conscientiousness, you might follow a regular schedule and have a knack for keeping track of details. 
        \nYou likely deliberate over options and work hard to achieve your goals. "
        "Coworkers and friends might see you as a reliable, fair person. 
        \nYou may tend to micromanage situations or tasks. 
        \nYou might also be cautious or difficult to please."
        
    else: # low
        "You have a low level of conscientiousness, which means you\n- Are less organized\n- Complete tasks in a less structured way"
        "- Take things as they come\n- Finish things at the last minute\n- and are impulsive"

        "A low conscientiousness score might mean you prefer a setting without structure. 
        \nYou may prefer doing things at your own pace to working on a deadline."
        "This might make you appear unreliable to others."
        
        
    if personality_scoreN > N_BOUNDARY:  # high
        "You have a high level of neuroticism. That means you,\n- Often feel vulnerable or insecure\n- Get stressed easily"
        "- Struggle with difficult situations\n- And have mood swings"

        "With high neuroticism, you may blame yourself when things go wrong. 
        \nYou might also get frustrated with yourself easily, especially if you make a mistake. "
        "Chances are, you’re also prone to worrying.
        \nBut you’re likely also more introspective than others, which helps you to examine and understand your feelings."
        
    else: # low
        "You have a low level of neuroticism, which means you\n- Keep calm in stressful situations\n- More optimistic"
        "- Worry less\n- And have a more stable mood"

        "A low neuroticism score can mean you’re confident. 
        \nYou may have more resilience and find it easy to keep calm under stress. 
        \nRelaxation might also come more easily to you. "
        "Try to keep in mind that this might not be as easy for those around you, so be patient."
        
        
    if personality_scoreO > O_BOUNDARY:  # high
        "You have a high level of openness. That means you,\n- Enjoy trying new things\n- Be more creative"
        "- Have a good imagination\n- And be willing to consider new ideas"

        "A high score on openness can mean you have broad interests. 
        \nYou may enjoy solving problems with new methods and find it easy to think about things in different ways. 
        \nBeing open to new ideas may help you adjust easily to change."
        "Just make sure to keep an eye out for any situations where you might need to establish boundaries, whether that be with family members or your work-life balance."
    
    else: # low
        "You have a low level of openness, which means you\n- Prefer to do things in a familiar way\n- Avoid change"
        "- And are more traditional in your thinking"

        "A low openness can mean you consider concepts in straightforward ways. 
        \nOthers likely see you as being grounded and down-to-earth."
    
    
    "That's all the test results we've got for you. I hope you understand yourself better now."
    
    "Thanks for taking this test and have a great day! :D"
    
    return
    