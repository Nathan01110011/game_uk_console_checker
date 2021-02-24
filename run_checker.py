import sys
import check_scheduler

if __name__ == "__main__":

    if sys.argv[1] == "ps":
        print("Starting PS check")
        check_scheduler.timer("ps")
    elif sys.argv[1] == "xbox":
        print("Starting XBOX check")
        check_scheduler.timer("xbox")
    elif sys.argv[1] == "both":
        print("Starting checks for PS and XBOX")
        check_scheduler.timer("both")
    else:
        print("unrecognised argument, choose either 'ps','xbox' or 'both'")
