import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc=new Scanner( System.in );
        int n=sc.nextInt();
        char gal[][] = new char [3][n];
        for(int i=0;i<3;i++){
            String a=sc.next();
            for(int j=0;j<n;j++)
            gal[i][j]=a.charAt(j);
        }
        for(int i=0;i<n;)
        {
            if(gal[0][i]=='#')//||gal[0][i+1]=='#')
            {
                System.out.print("#"); i++; continue;
            }
            if(gal[0][i]=='.' && gal[1][i]=='.' && gal[2][i]=='.')
            {
                i++; continue;
            }
            if(gal[0][i]=='.' && gal[0][i+2]=='.' && gal[2][i+1]=='.')
            System.out.print("A");
            else if(gal[1][i+1]=='.')
            {
                if(gal[0][i+1]=='.')
                System.out.print("U");
                else
                System.out.print("O");
            }
            else if(gal[1][i]=='.' && gal[1][i+2]=='.')
            System.out.print("I");
            //else if(gal[0][i]=='#')
            //System.out.print("#");
            else
            System.out.print("E");
            
            i+=3;
        }
        // System.out.println("XXXXXXXX");
    }
