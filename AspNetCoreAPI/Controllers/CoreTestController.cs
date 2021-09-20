using AspNetCoreAPI.Data;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace AspNetCoreAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CoreTestController : ControllerBase
    {

        readonly StudentContext _studentContext = new StudentContext();

        [Route("GetStudents")]
        [HttpGet]
        public IEnumerable<Student> GetStudents()
        {
            return _studentContext.GetStudents(student => student.Age >= 20);
        }
    }
}
