using System;
using System.Collections.Generic;
using System.Linq;

namespace Day53Leetcode2sum
{
    class Program
    {
        public int[] TwoSum(int[] nums, int target)
        {
            var set = new Dictionary<int, int>();
            for (var i = 0; i < nums.Length; i++)
            {
                var number = nums[i];
                if (set.ContainsKey(target - number))
                {
                    return new[] { set[target - number], i };
                }

                if (!set.ContainsKey(number))
                {
                    set.Add(number, i);
                }
            }

            static void Main(string[] args)
        {
            // https://www.sanfoundry.com/csharp-programs-reverse-string-predefined-function/

            List<int> arris = new List<int> { 2, 7, 11, 15 };
            int sumis = 9;
                Console.WriteLine(TwoSum(arris, sumis));
            Console.ReadLine();
        }
    }
}
