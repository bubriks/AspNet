using AspNetCoreAPI.Data;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

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
            Thread.Sleep(1000);
            return _studentContext.GetStudents(student => student.Age >= 20);
        }
    }
}
