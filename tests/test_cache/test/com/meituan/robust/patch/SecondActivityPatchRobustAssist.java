/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  android.os.Bundle
 *  android.support.v7.app.u
 *  com.meituan.sample.SecondActivity
 */
package com.meituan.robust.patch;

import android.os.Bundle;
import android.support.v7.app.u;
import com.meituan.robust.patch.SecondActivityPatch;
import com.meituan.sample.SecondActivity;

public class SecondActivityPatchRobustAssist
extends u {
    public static void staticRobustonCreate(SecondActivityPatch secondActivityPatch, SecondActivity secondActivity, Bundle bundle) {
        super.onCreate(bundle);
    }
}

