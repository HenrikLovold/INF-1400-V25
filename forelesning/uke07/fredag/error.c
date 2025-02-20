#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    FILE *fd = fopen("index", "r");
    if(fd == NULL) {
        int err = errno;
        printf("Unable to open index %d: %s\n", err, strerror(err));
        exit(1);
    }
    char buf[1000] = {0};
    fread(buf, 1, 999, fd);
    if(ferror(fd) != 0) {
        printf("Read error on index!\n");
        exit(1);
    }
    char *cur_line = NULL;
    char delim = '\n';
    char *bufferp = buf;
    char ibuf[1000] = {0};
    while(cur_line = strsep(&bufferp, &delim)) {
        FILE *ifd = fopen(cur_line, "r");
        if(ifd == NULL) continue;
        if(!fread(ibuf, 1, 999, ifd)) {
            fclose(ifd);
            continue;
        }
        printf("%s\n", ibuf);
        memset(ibuf, 0, 999);
        fclose(ifd);
    }
    fclose(fd);
    return 0;
}
