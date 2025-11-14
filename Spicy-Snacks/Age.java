
import java.util.Scanner;

public class Age{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter father's current age: ");
        int fathersAge = input.nextInt();
        System.out.print("Enter son's current age: ");
        int sonsAge = input.nextInt();
        int number_of_years = father_age - 2 * son_age;
        years_difference = Maths.abs(number_of_years);
        if(number_of_years > 0){
        System.out.printf("%d years ago, the father was twice as old as his son.", years_difference)
        }else if(number_of_years < 0){
            System.out.printf("In %d years, the father will be twice as old as his son.", years_difference)
        }else{
            System.out.print("Right now, the father is twice as old as his son")
        }
        
    }
}
