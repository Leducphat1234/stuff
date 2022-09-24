program Hien_thi_ten_ban_lop_truong;
uses crt, sysutils;
var monitor_name: string;
    lop: string[3];
    filelop: text;
    check: string;
    dir: string;
procedure write_and_save_monitor_name(dir: string);
begin
    write('Nhap ten ban lop truong lop ban: ');
    readln(monitor_name);
    Assign(filelop, dir + '\lop_truong\lop_truong_cua_' + lop + '.txt');
    Rewrite(filelop);
    writeln(filelop, monitor_name);
    close(filelop);
    writeln('Ban lop truong lop ban la ', monitor_name);
    delay(3000);
end;

begin
    ClrScr;
    dir:= 'C:\FPC\3.2.2\bin\i386-win32';
    write('Nhap lop cua ban (6a4, 7a7, 8a5, 9a3, ...): ');
    readln(lop);
    case lop[1] of
        '6' .. '9': {do nothing};
        else
        begin
            writeln('Ban nhap lop khong dung!');
            exit;
        end;
    end;
    case lop[3] of
        '1' .. '7': {do nothing};
        else
        begin
            writeln('Ban nhap lop khong dung!');
            exit;
        end;
    end;

    if not FileExists(dir + '\lop_truong\lop_truong_cua_' + lop + '.txt') then
    begin
        write_and_save_monitor_name(dir);
    end
    else
    begin
        Assign(filelop, dir + '\lop_truong\lop_truong_cua_' + lop + '.txt');
        Reset(filelop);
        readln(filelop, monitor_name);
        writeln('Ban lop truong lop ban ten la ', monitor_name);
        writeln;
        writeln('Ten ban lop truong lop ban co dung khong?');
        write('y/n: ');
        repeat
            readln(check);
        until (check = 'y') or (check = 'n');
        if check = 'y' then
        begin
            writeln('Cam on ban');
            delay(3000);
        end
        else if check = 'n' then
        begin
            write_and_save_monitor_name(dir);
        end;
    close(filelop);
    end;
end.
