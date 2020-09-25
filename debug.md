# pdb debug
```python
import pdb
...
pdb.set_trace()
...
```

```
    s(tep)
            Execute the current line, stop at the first possible occasion
            (either in a function that is called or in the current
            function).

    n(ext)
            Continue execution until the next line in the current function
            is reached or it returns.

    unt(il) [lineno]
            Without argument, continue execution until the line with a
            number greater than the current one is reached.  With a line
            number, continue execution until a line with a number greater
            or equal to that is reached.  In both cases, also stop when
            the current frame returns.

    j(ump) lineno
            Set the next line that will be executed.  Only available in
            the bottom-most frame.  This lets you jump back and execute
            code again, or jump forward to skip code that you don't want
            to run.

            It should be noted that not all jumps are allowed -- for
            instance it is not possible to jump into the middle of a
            for loop or out of a finally clause.

    r(eturn)
            Continue execution until the current function returns.

    retval
            Print the return value for the last return of a function.

    run [args...]
            Restart the debugged python program. If a string is supplied
            it is split with "shlex", and the result is used as the new
            sys.argv.  History, breakpoints, actions and debugger options
            are preserved.  "restart" is an alias for "run".

    c(ont(inue))
            Continue execution, only stop when a breakpoint is encountered.

    l(ist) [first [,last] | .]

            List source code for the current file.  Without arguments,
            list 11 lines around the current line or continue the previous
            listing.  With . as argument, list 11 lines around the current
            line.  With one argument, list 11 lines starting at that line.
            With two arguments, list the given range; if the second
            argument is less than the first, it is a count.

            The current line in the current frame is indicated by "->".
            If an exception is being debugged, the line where the
            exception was originally raised or propagated is indicated by
            ">>", if it differs from the current line.

    longlist | ll
            List the whole source code for the current function or frame.

    a(rgs)
            Print the argument list of the current function.

    p expression
            Print the value of the expression.

    pp expression
            Pretty-print the value of the expression.

    whatis arg
            Print the type of the argument.

    source expression
            Try to get source code for the given object and display it.
```
