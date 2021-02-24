import sys
import scheduler

if __name__ == "__main__":

    if sys.argv[1] == "ps":
        print("Starting PS check")
        scheduler.timer("ps")
    elif sys.argv[1] == "xbox":
        print("Starting XBOX check")
        scheduler.timer("xbox")
    elif sys.argv[1] == "both":
        print("Starting checks for PS and XBOX")
        scheduler.timer("both")
    else:
        print("unrecognised argument, choose either 'ps','xbox' or 'both'")
