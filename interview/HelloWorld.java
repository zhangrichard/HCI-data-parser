import java.util.*;
public class HelloWorld {

    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
        Student [] students = new Student [10];
        Student a = new Student();
        Student b = new Student();
        students[0] = a;
        students[1] = b;


        buildMap(students);
        
        System.err.println("Hello, World");
    }
    public static HashMap<Integer,Student> buildMap (Student[] students){
    	HashMap<Integer,Student> map = new HashMap<Integer,Student>();
    	for (Student s :students) map.put(s.getId(),s);
    		return map;

    }
    

}
class Student{
    	static int id = 0;
    	Integer getId(){
    		return new Integer(id);
    	}
    }
