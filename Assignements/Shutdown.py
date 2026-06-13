def shutdown():
    user_input=input("Do you want to shut down your computer? (Yes/ No): ")
    if user_input == "Yes":
        print("Shutting down...")
    elif user_input == "No":
        print ("Abort shutdown.")
    else:
        print('Invalid request.')

shutdown()
    
       