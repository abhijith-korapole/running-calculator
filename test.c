struct Test {
    int x;
};

int main()
{
    struct Test t = {5};
    struct Test *p = &t;

    printf("%d", p->x);
}