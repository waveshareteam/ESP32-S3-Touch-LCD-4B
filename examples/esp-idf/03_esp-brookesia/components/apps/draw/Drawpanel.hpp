#pragma once

#include <stddef.h>

#include "lvgl.h"
#include "esp_brookesia.hpp"

class Drawpanel: public ESP_Brookesia_PhoneApp
{
public:
    Drawpanel();
    ~Drawpanel();

    bool run(void);
    bool back(void);
    bool close(void);

    bool init(void) override;

private:
    static constexpr size_t MAX_DOTS = 128;
    static void touch_event_cb(lv_event_t *e);
    lv_obj_t *panel_obj = nullptr;
    lv_obj_t *dots[MAX_DOTS] = {};
    size_t next_dot = 0;
    size_t dot_count = 0;
    lv_point_t prev_point;
};
