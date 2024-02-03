struct node {
    int num;
    struct node* next;
};
struct node* make_circle(struct node* head)

Your Answer:
struct node* make_circle(struct node* head) {

 if (head == NULL) {

   return head;

 }

 struct node* cur = head;

 while (cur->next != NULL) {

  cur = cur->next;

 }

 cur->next = head;

}


 typedef struct Employee
 {
 char *first; // Employee's first name.
 char *last; // Employee's last name.
 int ID; // Employee ID.
 } Employee;

 Employee *makeArray(char **firstNames, char **lastNames, int *IDs, int n)
 {
    int i;
    Employee *array = (Employee*)malloc(
n*sizeof(Employee)
 );
    for (i = 0; i < n; i++)
    {
         array
[i]
 .first = (char*)malloc(
(strlen(firstNames[i])+1)*sizeof(char))
 );
         array[i].last = (char*)malloc(
(strlen(lastNames[i])+1)*sizeof(char))
 );
         strcpy(array[i].first, firstNames[i]);
         strcpy(array[i].last, lastNames[i]);
         array[i].ID = IDs[i];
    }
    return array;
 }
