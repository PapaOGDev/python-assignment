import java.util.Scanner;

public class StudentScores{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your first score: ");
        int firstScore = input.nextInt();
        System.out.print("Enter your second score: ");
        int secondScore = input.nextInt();
        System.out.print("Enter your third score: ");
        int thirdScore = input.nextInt();
        int average = (first_score + second_score + third_score)/3;
        
        if(average < 60):
            System.out.println("F")
        else if(average>=60 && average < 70):
            System.out.println("D")
        else if(average>=70 && average < 80):
            System.out.println("C")
        else if(average>=80 && average < 90):
            System.out.println("B")
        else if(average>=90 && average <=100):
            System.out.println("A")


    }
}
