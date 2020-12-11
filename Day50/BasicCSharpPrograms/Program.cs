using System;

namespace BasicCSharpPrograms
{
    class Program
    {

        static void printarray(int[] arr)
        {
            foreach(int i in arr)
            {
                Console.WriteLine(i);
            }
        }
        static void printmultiarray(int[] arr)
        {
            foreach(int i in arr)
            {
                foreach(int j in arr)
                {

                    Console.WriteLine(i);
                    Console.WriteLine(j);
                }
            }
        }
        public static void Main(string[] args)
        {
            int[] arris = new int[5];
            arris[0] = 2;
            arris[1] = 44;
            arris[2] = 32;
            arris[4] = 2222;
            //Console.WriteLine(arris[0]);
            int[,] twodarr = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };

            //printarray(arris);
            printmultiarray(twodarr);

            //for(int i = 0; i < arris.Length; i++)
            //{
            //    Console.WriteLine(arris[i]);
            //}

            //foreach(int i in arris)
            //{
            //    Console.WriteLine(i);
            //}
            Console.ReadLine();
        }

        
    }
}
