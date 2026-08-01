#include "Drawpanel.hpp"
#include "lvgl.h"

LV_IMG_DECLARE(img_app_drawpanel);

Drawpanel::Drawpanel() : ESP_Brookesia_PhoneApp("Drawpanel", &img_app_drawpanel, true)
{
}

Drawpanel::~Drawpanel()
{
}

bool Drawpanel::run(void)
{
    lv_area_t area = getVisualArea();
    int _width = area.x2 - area.x1;
    int _height = area.y2 - area.y1;

    panel_obj = lv_obj_create(lv_scr_act());
    lv_obj_set_size(panel_obj, _width, _height);
    lv_obj_align(panel_obj, LV_ALIGN_TOP_LEFT, 0, 0);

    next_dot = 0;
    dot_count = 0;
    for (size_t i = 0; i < MAX_DOTS; ++i) {
        dots[i] = nullptr;
    }

    lv_obj_add_event_cb(panel_obj, touch_event_cb, LV_EVENT_PRESSING, this);

    lv_obj_clear_flag(lv_scr_act(), LV_OBJ_FLAG_SCROLLABLE);
    lv_obj_clear_flag(lv_scr_act(), LV_OBJ_FLAG_SCROLL_CHAIN_HOR);
    lv_obj_clear_flag(lv_scr_act(), LV_OBJ_FLAG_SCROLL_CHAIN_VER);

    return true;
}

bool Drawpanel::back(void)
{
    notifyCoreClosed();

    return true;
}

bool Drawpanel::close(void)
{
    panel_obj = nullptr;
    next_dot = 0;
    dot_count = 0;
    for (size_t i = 0; i < MAX_DOTS; ++i) {
        dots[i] = nullptr;
    }

    return true;
}

bool Drawpanel::init(void)
{
    return true;
}

void Drawpanel::touch_event_cb(lv_event_t *e)
{
    Drawpanel *app = (Drawpanel *)lv_event_get_user_data(e);
    lv_indev_t *indev = lv_indev_get_act();
    lv_point_t point;

    if ((app == nullptr) || (app->panel_obj == nullptr) || (indev == nullptr)) {
        return;
    }

    lv_indev_get_point(indev, &point);

    if (app->dot_count == MAX_DOTS) {
        lv_obj_del(app->dots[app->next_dot]);
    } else {
        app->dot_count++;
    }

    lv_obj_t *dot = lv_obj_create(app->panel_obj);
    lv_obj_set_size(dot, 10, 10);                                // 设置圆点的大小
    lv_obj_set_pos(dot, point.x, point.y - 40);                       // 将圆点中心移到触摸点
    lv_obj_set_style_bg_color(dot, lv_color_make(255, 0, 0), 0); // 设置圆点颜色为红色
    lv_obj_set_style_radius(dot, 5, 0);                          // 设置圆角半径，使其为圆形

    app->dots[app->next_dot] = dot;
    app->next_dot = (app->next_dot + 1) % MAX_DOTS;
}
