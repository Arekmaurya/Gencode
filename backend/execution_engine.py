import subprocess
import time
from models import ExecuteResponse

def run_code(code: str, problem_id: str) -> ExecuteResponse:
    # A simple MVP code execution placeholder
    # CAUTION: Running arbitrary user code via subprocess is insecure for production.
    # This is an MVP and assumes local usage or restricted environment setup later.
    
    start_time = time.time()
    
    # We will write the code to a temporary file, then execute it with python
    try:
        with open("temp_exec.py", "w") as f:
            f.write(code)
            
        result = subprocess.run(
            ["python", "temp_exec.py"],
            capture_output=True,
            text=True,
            timeout=5 # 5 second timeout for code execution
        )
        
        exec_time = (time.time() - start_time) * 1000
        
        if result.returncode == 0:
            return ExecuteResponse(
                status="pass",
                output=result.stdout,
                execution_time_ms=exec_time
            )
        else:
            return ExecuteResponse(
                status="error",
                output=result.stderr,
                execution_time_ms=exec_time
            )
            
    except subprocess.TimeoutExpired:
        return ExecuteResponse(
            status="error",
            output="Execution timed out.",
            execution_time_ms=5000.0
        )
    except Exception as e:
         return ExecuteResponse(
            status="error",
            output=str(e),
            execution_time_ms=0.0
        )
