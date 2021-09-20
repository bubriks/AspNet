using System;
using System.Collections.Generic;
using System.Linq;

namespace AspNetFrameworkAPI.Data
{
    public class StudentContext
    {
        private Random rnd = new Random();

        public IEnumerable<Student> GetStudents(Func<Student, bool> predicate)
        {
            return GetRandomStudents().Where(predicate);
        }

        private List<Student> GetRandomStudents()
        {
            List<Student> students = new List<Student>();
            for (int i = 0; i < 1000; i++)
            {
                Student student = new Student
                {
                    Id = Guid.NewGuid().ToString(),
                    Age = rnd.Next(100),
                    FirstName = GenerateRandomText(rnd.Next(4, 12)),
                    LastName = GenerateRandomText(rnd.Next(1, 33))
                };
                students.Add(student);
            }
            return students;
        }

        private string GenerateRandomText(int length)
        {
            var stringChars = new char[length];
            // characters that can be used
            var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            for (int i = 0; i < stringChars.Length; i++)
            {
                stringChars[i] = chars[rnd.Next(chars.Length)];
            }

            return new String(stringChars);
        }
    }
}
