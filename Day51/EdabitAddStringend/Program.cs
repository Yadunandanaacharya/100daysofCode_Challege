//using System;
//using System.Collections.Generic;
////using System.Collection.Generics;

//namespace EdabitAddStringend
//{
//    class Program
//    {


//        static void Main(string[] args)
//        {
//            string[] Mainstr = {"clever", "meek", "hurried", "nice"};
//            string Endstr = "ly";
//            Console.WriteLine(Endstr);
//            Dictionary<int, string> Months = new Dictionary<int, string>()
//            {
//                { 1,"January" },{ 2,"January" },{ 3,"January" },{ 4,"January" },{5,"January" },{ 6,"January" },
//                { 7,"January" },{ 8,"January" },{ 9,"January" },{ 10,"January" },{ 11,"January" },{ 12,"January" }
//            };

//            for(int i = 0; i <= Months.Count; i++)
//            {
//                Console.WriteLine(Months[1]);
//            }




//            Console.ReadLine();
//        }
//    }
//}




using System;
using System.Collections.Generic;

class GFG
{

    // Main Method  
    static public void Main()
    {

        // Creating a dictionary 
        // using Dictionary<TKey,TValue> class 
        Dictionary<int, string> My_dict1 =
                       new Dictionary<int, string>();

        // Adding key/value pairs  
        // in the Dictionary 
        // Using Add() method 
        My_dict1.Add(1123, "Welcome");
        My_dict1.Add(1124, "to");
        My_dict1.Add(1125, "GeeksforGeeks");

        foreach (KeyValuePair<int, string> ele1 in My_dict1)
        {
            Console.WriteLine("{0} and {1}",
                      ele1.Key, ele1.Value);
        }
        Console.WriteLine();

        // Creating another dictionary 
        // using Dictionary<TKey,TValue> class 
        // adding key/value pairs without 
        // using Add method 
        Dictionary<string, string> My_dict2 =
                new Dictionary<string, string>(){
                                  {"a.1", "Dog"},
                                  {"a.2", "Cat"},
                                {"a.3", "Pig"} };

        foreach (KeyValuePair<string, string> ele2 in My_dict2)
        {
            Console.WriteLine("{0} and {1}", ele2.Key, ele2.Value);
        }
    }
}
