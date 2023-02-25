#include <time.h>

char *get_time()
{
    time_t ltime;
    time(&ltime);
    return ctime(&ltime);
}

