from flask import Flask,jsonify,request
app2=Flask(__name__)
@app2.route('/chatbot',methods=['POST'])
def chatbot():
    user_message=request.json.get('message')
    response_message=" "
    if user_message:
        user_message=user_message.lower()
        if "hello" in user_message:
            response_message="hello  how can i assist you ?"
        elif "how are you" in user_message:
            response_message="i am good!! what about you?" 
        elif "ok bye" in user_message:
            response_message="bye have a good day."  
        elif "how was the day today?" in user_message :
            response_message="it was a good thank you"
        elif "are you new in the bengaluru" in user_message :
             response_message="yes it been one month here in the bengaluru" 
        elif "for what you came here in the bengalure job or study?" in user_message:
            response_message="i came here for internship"     
        else:
            response_message="i dont have response for your question sorry" 
    else:
        response_message="please say something"         
    return jsonify({'response':response_message})         
if __name__ == '__main__':
     app2.run(debug=True)