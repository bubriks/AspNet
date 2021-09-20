using AspNetFrameworkAPI.Data;
using System.Collections.Generic;
using System.Web.Http;

namespace AspNetFrameworkAPI.Controllers
{
    public class FrameworkTestController : ApiController
    {

        readonly StudentContext _studentContext = new StudentContext();

        [HttpGet]
        public IEnumerable<Student> GetStudents()
        {
            return _studentContext.GetStudents(student => student.Age >= 20);
        }

    }
}
