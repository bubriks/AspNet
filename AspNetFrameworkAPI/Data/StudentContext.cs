using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace AspNetFrameworkAPI.Data
{
    public class StudentContext
    {
        static List<Student> students = new List<Student> {
            new Student {
                Id = 1,
                Age = 30,
                FirstName = "Simon",
                LastName = "Binyamin"
            },
            new Student {
                Id = 2,
                Age = 25,
                FirstName = "Ralfs",
                LastName = "Zangis"
            }
        };

        public IEnumerable<Student> GetStudents(Func<Student, bool> predicate)
        {
            return students.Where(predicate);
        }

    }

}
