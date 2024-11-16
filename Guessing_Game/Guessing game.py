import streamlit as st
st.title("Welcome")
st.write("Welcome to guessing game")
st.write("think a number between 1 and 100")
low=0
high=100
steps=0
while low<=high:
    mid=(low+high)//2
    responce=(input("is the number you guessed"+str(mid)+"(reply yes or low or high)"))
    if responce=="yes":
        steps+=1
        st.write(f"congrtulation")
        break
    elif responce=="low":
        steps+=1
        high=mid-1
    elif responce=="high":
        steps+=1
        low=mid+1
    else:
        st.write(f"invalid statement")
st.write(f"it took",steps,"steps.")
