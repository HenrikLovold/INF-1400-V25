const std = @import("std");

pub fn main() !u8 {
    const cwd = std.fs.cwd();
    const fd = try cwd.openFile("index", .{});
    var buf: [1000]u8 = undefined;
    const data_size = try fd.readAll(&buf);
    fd.close();

    var lines = std.mem.tokenizeAny(u8, buf[0..data_size], "\n");
    var ibuf: [1000]u8 = undefined;
    while(lines.next()) |line| {
        const ifile = cwd.openFile(line, .{}) catch continue;
        defer ifile.close();
        const len = ifile.readAll(&ibuf) catch continue;
        const printable = ibuf[0..len];
        std.debug.print("{s}\n", .{printable});
    }
    return 0;
}
