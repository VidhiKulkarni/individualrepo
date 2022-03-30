# Function to print the pattern of a fish - Gigi Guan
# over N rows - Gigi Guan
def printFish(N) :
    spaces1 = ""; spaces2 = "";
    stars1 = "*"; stars2 = "";
    for i in range(N) :
        spaces1 += ' ';

    spaces2 = spaces1;

    for i in range( 2 * N + 1) :
        # For upper part
        if (i < N) :
            print(spaces1,end="");
            print(stars1,end="");
            print(spaces1,end="");
            print(spaces1,end="");
            print(stars2);
            spaces1 = spaces1[:-1]
            stars1 += "**";
            stars2 += "*";

        # For middle part
        if (i == N) :
            print(spaces1,end="");
            print(stars1,end="");
            print(spaces1,end="");
            print(spaces1,end="");
            print(stars2);

        # For lower part
        if (i > N) :
            spaces1 += ' ';
            stars1 = stars1[:-1];
            stars1 = stars1[:-1];
            stars2 = stars2[:-1];

            print(spaces1,end="");
            print(stars1,end="")
            print(spaces1,end="");
            print(spaces1,end="");
            print(stars2);

# Driver Code  - Gigi Guan
if __name__ == "__main__" :
    # input for user to indicate how many rows of the fish they want - Gigi Guan
    N = int(input("How many rows?"))
    printFish(N);
