import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FeaturePostComponent } from './feature-post.component';

describe('FeaturePostComponent', () => {
  let component: FeaturePostComponent;
  let fixture: ComponentFixture<FeaturePostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FeaturePostComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FeaturePostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
