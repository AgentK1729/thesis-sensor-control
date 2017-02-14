// ---------------------------------------------------------------------------
// Example NewPing library sketch that does a ping about 20 times per second.
// ---------------------------------------------------------------------------

#include <NewPing.h>

#define TRIGGER_GREEN  6
#define ECHO_GREEN     7

#define TRIGGER_YELLOW  3
#define ECHO_YELLOW     2

#define TRIGGER_RED  10
#define ECHO_RED     11

#define MAX_DISTANCE 200

NewPing sonar_green(TRIGGER_GREEN, ECHO_GREEN, MAX_DISTANCE);

NewPing sonar_red(TRIGGER_RED, ECHO_RED, MAX_DISTANCE);

NewPing sonar_yellow(TRIGGER_YELLOW, ECHO_YELLOW, MAX_DISTANCE);

void setup() {
  Serial.begin(115200);
}

void loop() {
  unsigned int g_dist = sonar_green.ping_cm();
  unsigned int r_dist = sonar_red.ping_cm();
  unsigned int y_dist = sonar_yellow.ping_cm();
  Serial.print(g_dist);
  Serial.print("\t");
  Serial.print(r_dist);
  Serial.print("\t");
  Serial.print(y_dist);
  Serial.print("\t");
  Serial.print("\n");
  delay(1000);
}
