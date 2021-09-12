using AspNetFrameworkAPI.Data;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading;
using System.Web.Http;

namespace AspNetFrameworkAPI.Controllers
{
    public class FrameworkTestController : ApiController
    {

        readonly StudentContext _studentContext = new StudentContext();

        [HttpGet]
        public IEnumerable<Student> GetStudents()
        {
            Thread.Sleep(1000);
            return _studentContext.GetStudents(student => student.Age >= 20);
        }

    }
}
