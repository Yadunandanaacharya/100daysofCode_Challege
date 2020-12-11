using System;

namespace jaggedarray
{
    class Program
    {
        static void printarr(int[] arr)
        {
            foreach(int i in arr)
            {
                Console.WriteLine(i + " ");
            }
        }
        static void Main(string[] args)
        {
            int[] arr = { 2, 1, 4, 5, 3 };
            Array.Sort(arr);
            printarr(arr);
            Console.ReadLine();
        }
    }
}
