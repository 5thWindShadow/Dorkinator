import urllib.parse

def intro():
    print("\033[1;35;40m       _____")
    print("      //    \ ")
    print("     //      \ ")
    print("    //        \ ")
    print("   //          \ ")
    print("  //            \ ")
    print(" //              \  ")
    print("//                \ ")
    print("\                 //")
    print(" \ Dorkinator[<] //")
    print("  \_____________//")
    print("   ;-----------; \n")
    print("Welcome to Dorkinator \n")
    print("by : 5thWindShadow")
    print("Ver 1.0 \n ")

def option():
    print("1 - <!>ALL OPTIONS<!>")
    print("66 - ALL Information Gathering")
    print("99 - ALL Vulnerability Parameters \n")

    print(" <----Information Gathering----> ")
    print("2 - Directory Listing. ")
    print("3 - Database Related. ")
    print("4 - Authentication Related. ")
    print("5 - Juicy Files. ")
    print("6 - Sensitive Informations. ")
    print("7 - Code Leaks. \n")

    print(" <----Vulnerability Parameters----> ")
    print("8 - Cross Site Scripting(XSS)")
    print("9 - SQL Injection(SQLi)")
    print("10 - Server-side Request Forgery(SSRF)")
    print("11 - Local File Inclusion(LFI)")
    print("12 - Remote Code Execution(RCE)")
    print("13 - PHP Extension")
    print("14 - File Upload")
    print("15 - Security Misconfiguration \n")

def continue_tool():
    while True:
        choice = input("Do you want to use the tool again? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def dirlist(x):
    x_encoded = urllib.parse.quote(x)
    
    directory_listing = "Directory Listing :\n"
    directory_listing += "\033]8;;https://www.google.com/search?q=site:" + x_encoded + "%20intitle:'Index of' inurl:/parent-directory%20%7C%20inurl:/admin%20%7C%20inurl:/backup%20%7C%20inurl:config%20%7C%20inurl:/logs\033\\"
    directory_listing += "www.google.com/search?q=site:" + x_encoded + "%20intitle:'Index of' inurl:/parent-directory%20%7C%20inurl:/admin%20%7C%20inurl:/backup%20%7C%20inurl:config%20%7C%20inurl:/logs\n"
    directory_listing += "\033]8;;\033\\"
    return directory_listing

def dbrel(x):
    x_encoded = urllib.parse.quote(x)

    database_related = "Database Related :\n"
    database_related += "\033]8;;https://www.google.com/search?q=site:" + x_encoded + "%20inurl:/phpmyadmin/index.php%20%7C%20inurl:/db/websql/%20%7C%20inurl:/phpPgAdmin/index.php%20%7C%20intext:\"phpMyAdmin%20MySQL-Dump\"%20%7C%20filetype:sql%20%7C%20intext:\"phpPgAdmin%20—%20Login\"\033\\"
    database_related += "www.google.com/search?q=site:" + x_encoded + "%20inurl:/phpmyadmin/index.php%20%7C%20inurl:/db/websql/%20%7C%20inurl:/phpPgAdmin/index.php%20%7C%20intext:\"phpMyAdmin%20MySQL-Dump\"%20%7C%20filetype:sql%20%7C%20intext:\"phpPgAdmin%20—%20Login\"\n"
    database_related += "\033]8;;\033\\"
    return database_related

def authrel(x):
    x_encoded = urllib.parse.quote(x)

    authentication_related = "Authentication Related :\n"
    authentication_related += "\033]8;;https://www.google.com/search?q=site:" + x_encoded + "%20intitle:\"Login\"%20inurl:/admin%20%7C%20intitle:\"Login\"%20inurl:/login%20%7C%20inurl:\"/admin/login.php\"\033\\"
    authentication_related += "www.google.com/search?q=site:" + x_encoded + "%20intitle:\"Login\"%20inurl:/admin%20%7C%20intitle:\"Login\"%20inurl:/login%20%7C%20inurl:\"/admin/login.php\"\n"
    authentication_related += "\033]8;;\033\\"
    return authentication_related

def juicy(x):
    x_encoded = urllib.parse.quote(x)

    juicy_files = "Juicy Files:\n"
    juicy_files += "\033]8;;https://www.google.com/search?q=site:" + x_encoded + "%20ext:log%20%7C%20ext:txt%20%7C%20ext:conf%20%7C%20ext:cnf%20%7C%20ext:ini%20%7C%20ext:env%20%7C%20ext:sh%20%7C%20ext:bak%20%7C%20ext:backup%20%7C%20ext:swp%20%7C%20ext:old%20%7C%20ext:~%20%7C%20ext:git%20%7C%20ext:svn%20%7C%20ext:htpasswd%20%7C%20ext:htaccess\033\\"
    juicy_files += "www.google.com/search?q=site:" + x_encoded + "%20ext:log%20%7C%20ext:txt%20%7C%20ext:conf%20%7C%20ext:cnf%20%7C%20ext:ini%20%7C%20ext:env%20%7C%20ext:sh%20%7C%20ext:bak%20%7C%20ext:backup%20%7C%20ext:swp%20%7C%20ext:old%20%7C%20ext:~%20%7C%20ext:git%20%7C%20ext:svn%20%7C%20ext:htpasswd%20%7C%20ext:htaccess\n"
    juicy_files += "\033]8;;\033\\"
    return juicy_files

def sensitive(x):
    x_encoded = urllib.parse.quote(x)

    sensitive_info = "Sensitive Information:\n"
    sensitive_info += "\033]8;;https://www.google.com/search?q=site:" + x_encoded + "%20inurl:email=%20%7C%20inurl:phone=%20%7C%20inurl:password=%20%7C%20inurl:secret=%20%7C%20inurl:paswd=\033\\"
    sensitive_info += "www.google.com/search?q=site:" + x_encoded + "%20inurl:email=%20%7C%20inurl:phone=%20%7C%20inurl:password=%20%7C%20inurl:secret=%20%7C%20inurl:paswd=\n"
    sensitive_info += "\033]8;;\033\\"
    return sensitive_info

def codeleaks(x):
    x_encoded = urllib.parse.quote(x)

    code_leaks = "Code Leaks:\n"
    code_leaks += "\033]8;;https://www.google.com/search?q=site:pastebin.com%20%22" + x_encoded + "%22\033\\"
    code_leaks += "www.google.com/search?q=site:pastebin.com%20%22" + x_encoded + "%22\n"
    code_leaks += "\033]8;;https://www.google.com/search?q=site:jsfiddle.net%20%22" + x_encoded + "%22\033\\"
    code_leaks += "www.google.com/search?q=site:jsfiddle.net%20%22" + x_encoded + "%22\n"
    code_leaks += "\033]8;;https://www.google.com/search?q=site:codebeautify.org%20%22" + x_encoded + "%22\033\\"
    code_leaks += "www.google.com/search?q=site:codebeautify.org%20%22" + x_encoded + "%22\n"
    code_leaks += "\033]8;;https://www.google.com/search?q=site:codepen.io%20%22" + x_encoded + "%22\033\\"
    code_leaks += "www.google.com/search?q=site:codepen.io%20%22" + x_encoded + "%22\n"
    code_leaks += "\033]8;;\033\\"
    return code_leaks


def xss(x):
    x_encoded = urllib.parse.quote(x)

    xss_search = "Cross Site Scripting (XSS):\n"
    xss_search += "\033]8;;https://www.google.com/search?q=inurl:q=%20%7C%20inurl:s=%20%7C%20inurl:search=%20%7C%20inurl:query=%20%7C%20inurl:keyword=%20%7C%20inurl:lang=%20inurl:%3A" + x_encoded + "\033\\"
    xss_search += "www.google.com/search?q=inurl:q=%20%7C%20inurl:s=%20%7C%20inurl:search=%20%7C%20inurl:query=%20%7C%20inurl:keyword=%20%7C%20inurl:lang=%20inurl:%3A" + x_encoded + "\n"
    xss_search += "\033]8;;\033\\"
    return xss_search

def sqli(x):
    x_encoded = urllib.parse.quote(x)

    sqli_search = "SQL Injection (SQLi):\n"
    sqli_search += "\033]8;;https://www.google.com/search?q=inurl:id=%20%7C%20inurl:pid=%20%7C%20inurl:category=%20%7C%20inurl:cat=%20%7C%20inurl:action=%20%7C%20inurl:sid=%20%7C%20inurl:dir=%20inurl:%3A" + x_encoded + "\033\\"
    sqli_search += "www.google.com/search?q=inurl:id=%20%7C%20inurl:pid=%20%7C%20inurl:category=%20%7C%20inurl:cat=%20%7C%20inurl:action=%20%7C%20inurl:sid=%20%7C%20inurl:dir=%20inurl:%3A" + x_encoded + "\n"
    sqli_search += "\033]8;;\033\\"
    return sqli_search

def ssrf(x):
    x_encoded = urllib.parse.quote(x)

    ssrf_search = "Server-side Request Forgery (SSRF):\n"
    ssrf_search += "\033]8;;https://www.google.com/search?q=inurl:http%20%7C%20inurl:url=%20%7C%20inurl:path=%20%7C%20inurl:dest=%20%7C%20inurl:html=%20%7C%20inurl:data=%20%7C%20inurl:domain=%20%7C%20inurl:page=%20inurl:%3A" + x_encoded + "\033\\"
    ssrf_search += "www.google.com/search?q=inurl:http%20%7C%20inurl:url=%20%7C%20inurl:path=%20%7C%20inurl:dest=%20%7C%20inurl:html=%20%7C%20inurl:data=%20%7C%20inurl:domain=%20%7C%20inurl:page=%20inurl:%3A" + x_encoded + "\n"
    ssrf_search += "\033]8;;\033\\"
    return ssrf_search

def lfi(x):
    x_encoded = urllib.parse.quote(x)
    
    lfi_search = "Local File Inclusion (LFI):\n"
    lfi_search += "\033]8;;https://www.google.com/search?q=inurl:include%20%7C%20inurl:dir%20%7C%20inurl:detail=%20%7C%20inurl:file=%20%7C%20inurl:folder=%20%7C%20inurl:inc=%20%7C%20inurl:locate=%20%7C%20inurl:doc=%20%7C%20inurl:conf=%20inurl:%3A" + x_encoded + "\033\\"
    lfi_search += "www.google.com/search?q=inurl:include%20%7C%20inurl:dir%20%7C%20inurl:detail=%20%7C%20inurl:file=%20%7C%20inurl:folder=%20%7C%20inurl:inc=%20%7C%20inurl:locate=%20%7C%20inurl:doc=%20%7C%20inurl:conf=%20inurl:%3A" + x_encoded + "\n"
    lfi_search += "\033]8;;\033\\"
    return lfi_search

def rce(x):
    x_encoded = urllib.parse.quote(x)

    rce_search = "Remote Code Execution (RCE):\n"
    rce_search += "\033]8;;https://www.google.com/search?q=inurl:cmd%20%7C%20inurl:exec=%20%7C%20inurl:query=%20%7C%20inurl:code=%20%7C%20inurl:do=%20%7C%20inurl:run=%20%7C%20inurl:read=%20%7C%20inurl:ping=%20inurl:%3A" + x_encoded + "\033\\"
    rce_search += "www.google.com/search?q=inurl:cmd%20%7C%20inurl:exec=%20%7C%20inurl:query=%20%7C%20inurl:code=%20%7C%20inurl:do=%20%7C%20inurl:run=%20%7C%20inurl:read=%20%7C%20inurl:ping=%20inurl:%3A" + x_encoded + "\n"
    rce_search += "\033]8;;\033\\"
    return rce_search

def phpe(x):
    phpe_search = "PHP Extension (PHPE):\n"
    phpe_search += "\033]8;;https://www.google.com/search?q=site:" + x + "%20ext:php%20inurl:%3F\033\\"
    phpe_search += "www.google.com/search?q=site:" + x + "%20ext:php%20inurl:%3F\n"
    phpe_search += "\033]8;;\033\\"
    return phpe_search

def fileup(x):
    file_upload_search = "File Upload:\n"
    file_upload_search += "\033]8;;https://www.google.com/search?q=site:" + x + "%20%22choose%20file%22\033\\"
    file_upload_search += "www.google.com/search?q=site:" + x + "%20%22choose%20file%22\n"
    file_upload_search += "\033]8;;\033\\"
    return file_upload_search

def miscon(x):
    x_encoded = urllib.parse.quote(x)
    
    miscon_search = "Miscellaneous Indexes:\n"
    miscon_search += "\033]8;;https://www.google.com/search?q=site:" + x_encoded + "%20intitle:index%20of%20smtp%20%7C%20intitle:index%20of%20kk%20%7C%20intitle:index%20of%20ssh%20%7C%20intitle:index%20of%20ftp\033\\"
    miscon_search += "www.google.com/search?q=site:" + x_encoded + "%20intitle:index%20of%20smtp%20%7C%20intitle:index%20of%20kk%20%7C%20intitle:index%20of%20ssh%20%7C%20intitle:index%20of%20ftp\n"
    miscon_search += "\033]8;;\033\\"
    return miscon_search



def runall(x):
    print("All Options")

def main():
    while True:
        intro()
        
        target = input("Enter your target(ex: example.com): ")
        print("[>] ", target, " [<]\n")
        print(" SELECT... \n")
        option()

        options = input("Choose : ")
        print(" ")
        if int(options) == 2:
            result2 = dirlist(target)
            print(result2)
            if not continue_tool():
             break
        elif int(options) == 3:
            result3 = dbrel(target)
            print(result3)
            if not continue_tool():
             break
        elif int(options) == 4:
            result4 = authrel(target)
            print(result4)
            if not continue_tool():
             break
        elif int(options) == 5:
            result5 = juicy(target)
            print(result5)
            if not continue_tool():
             break
        elif int(options) == 6:
            result6 = sensitive(target)
            print(result6)
            if not continue_tool():
             break
        elif int(options) == 7:
            result7 = codeleaks(target)
            print(result7)
            if not continue_tool():
             break
        elif int(options) == 66:
            result2 = dirlist(target)
            print(result2)
            result3 = dbrel(target)
            print(result3)
            result4 = authrel(target)
            print(result4)
            result5 = juicy(target)
            print(result5)
            result6 = sensitive(target)
            print(result6)
            result7 = codeleaks(target)
            print(result7)
            if not continue_tool():
             break
        elif int(options) == 8:
            result8 = xss(target)
            print(result8)
            if not continue_tool():
             break
        elif int(options) == 9:
            result9 = sqli(target)
            print(result9)
            if not continue_tool():
             break
        elif int(options) == 10:
            result10 = ssrf(target)
            print(result10)
            if not continue_tool():
             break
        elif int(options) == 11:
            result11 = lfi(target)
            print(result11)
            if not continue_tool():
             break
        elif int(options) == 12:
            result12 = rce(target)
            print(result12)
            if not continue_tool():
             break
        elif int(options) == 13:
            result13 = phpe(target)
            print(result13)
            if not continue_tool():
             break
        elif int(options) == 14:
            result14 = fileup(target)
            print(result14)
            if not continue_tool():
             break
        elif int(options) == 15:
            result15 = miscon(target)
            print(result15)
            if not continue_tool():
             break
        elif int(options) == 99:
            result8 = xss(target)
            print(result8)
            result9 = sqli(target)
            print(result9)
            result10 = ssrf(target)
            print(result10)
            result11 = lfi(target)
            print(result11)
            result12 = rce(target)
            print(result12)
            result13 = phpe(target)
            print(result13)
            result14 = fileup(target)
            print(result14)
            result15 = miscon(target)
            print(result15)
            if not continue_tool():
             break
        elif int(options) == 1:
            result2 = dirlist(target)
            print(result2)
            result3 = dbrel(target)
            print(result3)
            result4 = authrel(target)
            print(result4)
            result5 = juicy(target)
            print(result5)
            result6 = sensitive(target)
            print(result6)
            result7 = codeleaks(target)
            print(result7)
            result8 = xss(target)
            print(result8)
            result9 = sqli(target)
            print(result9)
            result10 = ssrf(target)
            print(result10)
            result11 = lfi(target)
            print(result11)
            result12 = rce(target)
            print(result12)
            result13 = phpe(target)
            print(result13)
            result14 = fileup(target)
            print(result14)
            result15 = miscon(target)
            print(result15)
            if not continue_tool():
             break
        else:
            print("Choose the number in the options \n")

            if not continue_tool():
             break

if __name__ == "__main__":
    main()
