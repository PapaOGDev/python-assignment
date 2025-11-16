
import java.util.Scanner;

public class Operation{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your first number: ");
        int firstNumber = input.nextInt();
        System.out.print("Enter your operator: ");
        String operator = input.nextLine();
        System.out.print("Enter your second number: ");
        int secondNumber = input.nextInt();
        result = 0;
        if(sign == "+")
            result = first_number + second_number;
        else if(sign == "-")
            result = first_number - second_number;
        else if(sign == "*")
            result = first_number * second_number;
        else if(sign == "/"){
            result = first_number / second_number;
        }
        System.out.print(result)
        
      

    }
}

